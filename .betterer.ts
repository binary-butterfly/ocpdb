// @ts-expect-error bettererfly is installed globally in the docker image
import {mypy, ruff} from '@common/bettererfly';

export default {
    mypy: () => mypy({}).include('./webapp/**/*.py*'),
    ruff: () => ruff({}).include('./webapp/**/*.py*'),
};
