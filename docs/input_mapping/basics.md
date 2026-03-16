# Mapping basics

Some rules apply to all importers, they are collected in this document.

* `id`s and `uid`s should be unique in scope of the data source. Therefore, `id`s and `uid`s are transformed
  into `uid` when saving the object, and to `original_id` and `original_uid` when outputting it. At mapper definition
  files, we always speak of `uid` for these transformed fields.
