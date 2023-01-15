## Deduplication Strategy

OCPDB is able to import official static data from Bundesnetzagentur as well as dynamic data from several operators.
Sadly, BNetzA data lacks the central identifier, the EVSEID, so we try to match static BNetzA data based on multiple
other parameters of a location:

* distance
* address
* operator name
* evse count

The matching algorithm first queries for any charge station in a square of +/- 250 m in every direction. Any result
in this list of locations will be part of a more detailed calculation.

The algorithm calculates a float factor of the probability if static location A and dynamic location B is the same
location. The factor is between 0 till 1. If there are multiple candidates, the highest factor wins. If the highest 
factor is below a defined threshold (default 0.25, can be changed by `config.yaml` by changing 
`MATCHING_FACTOR_THRESHOLD`), the relation will be ignored, too.

All factors will be multiplied to get the final factor:

```math
f_{all} = f_{distance} * f_{address} * f_{operator\_name} * f_{evse\_count} 
```

The location factor `f_distance` uses a Gaussian function in order to get high values for a range of shorter distances,
but very low values for long distances. With `distance` in meters its calculated by:

```math
f_{distance} = exp(-1 * {distance^2 \over 10000})
```

The address factor uses an NGram comparison between both `address` values. The string is transformed to lower case
before in order to reduce the noise by wrong cases.

```math
f_{address} = ngram(location_a.address, location_b.address)
```

The operator name factor also uses NGram - if the operator exists at all on both locations. If not, the factor 
will be ignored and is still 1.

```math
f_{operator\_name} = ngram(location_a.operator.name, location_b.operator.name)
```

The evse count factor is 1 for an equal amount of evses and gets less and less the greater the difference is:

```math
f_{evse\_count} = 1 - 0.4 * {{abs(len(location_a.evses) - len(location_b.evses))} 
    \over {abs(len(location_a.evses) - len(location_b.evses)) + 1}}
```
