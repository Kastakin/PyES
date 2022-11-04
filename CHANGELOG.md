# Version v0.4.1

## Enhancements
* Adopt different solid computation logic ([](https://github.com/Kastakin/PyES/commit/))

## Fixes
* Export solid distributions in excel/csv ([e1aead0](https://github.com/Kastakin/PyES/commit/e1aead03c50b4de9546380654e51ce0aa4a22213))
* Handle paths with dots in them ([b8d56b6](https://github.com/Kastakin/PyES/commit/b8d56b646cebc964519fa98c42d541dfabc7c1a3))
* Remove print statements ([89a5b1d](https://github.com/Kastakin/PyES/commit/89a5b1d930512209733b2f6fbde3ce4c60529d89))

## Chores
* Run changelog script as tbump hook ([5e09d2e](https://github.com/Kastakin/PyES/commit/5e09d2e51a0f611b46efa446a7770c8eabd23819))
* Create changelog before bumping version ([6c74903](https://github.com/Kastakin/PyES/commit/6c74903142c547b0480f109891af25b53729f769))
* Remove module not used anymore ([ffe0c6e](https://github.com/Kastakin/PyES/commit/ffe0c6ec1fb76bf6dea320042f3e915675b5608a))
* Refactoring and typos ([ada11de](https://github.com/Kastakin/PyES/commit/ada11de3d5ec5b28cc83648babf2058b5bb5bf46))
* Use ubuntu-latest in github runners ([b150c7f](https://github.com/Kastakin/PyES/commit/b150c7fc3ed2b0583fa0a85cc304e0818c48c487))
* Ignore matplotlib to reduce installer size ([d9300d7](https://github.com/Kastakin/PyES/commit/d9300d7256f5fa88efc198d53af388d1b8a7204e))
* Remove unused imports ([65476f4](https://github.com/Kastakin/PyES/commit/65476f43464d93302825a41b06e7bd6980e4fd08))
* Update CHANGELOG ([ae83da0](https://github.com/Kastakin/PyES/commit/ae83da0a3b0481d577834bdca52f3a5b5fc8857c))


# Version v0.4.0

## Features
* Compute solids uncertainty ([7d95e838](https://github.com/Kastakin/PyES/commit/7d95e838d3984ce47d2851e4ded61c9ffedece17))
* Add profiling and benchmarks utilities ([1c150c81](https://github.com/Kastakin/PyES/commit/1c150c812b88617fa98921b05641e8283adee599))
* Allow change colors in plots ([130a92a6](https://github.com/Kastakin/PyES/commit/130a92a66bca0cb7505212d9d9645c95b4d29ea0))

## Enhancements
* Vectorize Jacobian computation ([a72a77e2](https://github.com/Kastakin/PyES/commit/a72a77e2dacfbbfda7f17e6dd75311d39ea49094))
* Minor optimization in speciesConcentrations ([4635b2f1](https://github.com/Kastakin/PyES/commit/4635b2f101f166fcbef24db79a9b2ce85341639d))
* Vectorize error computation operations ([fe215863](https://github.com/Kastakin/PyES/commit/fe215863eaee23ff1679b128afe385a066016e66))
* Testing different damping parameters ([f44770a0](https://github.com/Kastakin/PyES/commit/f44770a012f3d3dc21aa4d9fd548ac15a27f4583))
* Avoid useless nested for loop ([cb413356](https://github.com/Kastakin/PyES/commit/cb41335614ee4276f33995819d00e8fe56e57c0a))
* Allow saving and loading to allow testing ([41fbcada](https://github.com/Kastakin/PyES/commit/41fbcadac323b44bc34dcdadf2f46fc75892cce9))
* Square color pickers in plot window ([ff352c41](https://github.com/Kastakin/PyES/commit/ff352c413f0deea59d0d1914343d5e34d9740b0c))

## Fixes
* Solid sigma is zero if no precipitation ([20b91d54](https://github.com/Kastakin/PyES/commit/20b91d54d5e0b164e114d47465eaafb00890223e))
* Use dummy variable in for loops if possible ([3dc1bc5e](https://github.com/Kastakin/PyES/commit/3dc1bc5e5ea5ae1b90c2d4492a5f154872db757b))
* Avoid useless numpy errors printing ([7d2a2af2](https://github.com/Kastakin/PyES/commit/7d2a2af2aadb31507360852b640d3377782ba467))
* Revert a0 change in damping ([00580970](https://github.com/Kastakin/PyES/commit/00580970dabf471aebf9b351af8cd948ddc558c7))
* Reduce string formatting in logging calls ([97ca1ae0](https://github.com/Kastakin/PyES/commit/97ca1ae0eb2c2b7d126dbc4d0f7c18d5511afcb3))
* Correctly handle checkbox delegate ([66e10e17](https://github.com/Kastakin/PyES/commit/66e10e171240b43d26b5535026c3c97e652f1b4e))
* Correct help_website placeholder link ([a0ac6c2b](https://github.com/Kastakin/PyES/commit/a0ac6c2be460d74b881ecafffe4a55f7df941358))
* Remove unused import ([47f61887](https://github.com/Kastakin/PyES/commit/47f618874e3141242a87239aeb6a97bb4618015e))
* Relax damping routine convergence ([4a45242a](https://github.com/Kastakin/PyES/commit/4a45242a967fd13968465c51eb9458089e7915d3))
* Relax conv condition for c~=0 ([c40c5995](https://github.com/Kastakin/PyES/commit/c40c5995d4b07681d7b47e93911da12999a13dcc))

## Chores
* Fix bump script ([a5bf778a](https://github.com/Kastakin/PyES/commit/a5bf778a352ab7a9924fcdc86a0a2a0eb8a515b0))
* Update build deps ([c3895dff](https://github.com/Kastakin/PyES/commit/c3895dff52f2440d41113ea829d140fc04e55a3f))
* Add pycharm files to .gitignore ([4010d7a2](https://github.com/Kastakin/PyES/commit/4010d7a239c8b5c4ac9bbc674573e8fbd234fb27))
* Poetry update ([c9a7d58a](https://github.com/Kastakin/PyES/commit/c9a7d58a9d240bd2a8acb5323125f69ff2c246e8))
* Script for version bumping/release notes ([03bd378c](https://github.com/Kastakin/PyES/commit/03bd378c012d67704e963a0445833b2201212ad3))
* Update pre-commit hooks ([a749bb27](https://github.com/Kastakin/PyES/commit/a749bb270014e2ec997d5d5a5d4662ac42b072eb))
* Move to stable pyqtrgaph ([c24ab1e4](https://github.com/Kastakin/PyES/commit/c24ab1e412a1449dfabf94e6140881bd607a8463))
* Remove useless readme in icon folder ([2d0c2cc1](https://github.com/Kastakin/PyES/commit/2d0c2cc1440ca0325ffbee92d42f7022ff47269c))
* Add scripts to generate icons ([217c13a6](https://github.com/Kastakin/PyES/commit/217c13a6027c832c882e70d1318140c2a0656908))
* Better naming DBH function ([5694e9f5](https://github.com/Kastakin/PyES/commit/5694e9f5ad306c4b4a04a0f3a3344c41f82815ab))

## Others
* to 0.4.0 ([5c61c684](https://github.com/Kastakin/PyES/commit/5c61c684bce0bf4348cc0bab84ec999480cd8bc1))


