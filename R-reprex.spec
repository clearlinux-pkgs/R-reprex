#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reprex
Version  : 0.3.0
Release  : 27
URL      : https://cran.r-project.org/src/contrib/reprex_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reprex_0.3.0.tar.gz
Summary  : Prepare Reproducible Example Code via the Clipboard
Group    : Development/Tools
License  : MIT
Requires: R-callr
Requires: R-clipr
Requires: R-fs
Requires: R-rlang
Requires: R-rmarkdown
Requires: R-whisker
Requires: R-withr
BuildRequires : R-callr
BuildRequires : R-clipr
BuildRequires : R-devtools
BuildRequires : R-fs
BuildRequires : R-rlang
BuildRequires : R-rmarkdown
BuildRequires : R-whisker
BuildRequires : R-withr
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# reprex <img src="man/figures/logo.png" align="right" height="139" />
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/reprex)](https://cran.r-project.org/package=reprex)
[![Travis-CI Build
Status](https://travis-ci.org/tidyverse/reprex.svg?branch=master)](https://travis-ci.org/tidyverse/reprex)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/tidyverse/reprex?branch=master&svg=true)](https://ci.appveyor.com/project/tidyverse/reprex)
[![Coverage
status](https://codecov.io/gh/tidyverse/reprex/branch/master/graph/badge.svg)](https://codecov.io/github/tidyverse/reprex?branch=master)
[![lifecycle](https://img.shields.io/badge/lifecycle-stable-brightgreen.svg)](https://www.tidyverse.org/lifecycle/#stable)

%prep
%setup -q -c -n reprex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571888668

%install
export SOURCE_DATE_EPOCH=1571888668
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reprex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reprex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reprex
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reprex || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reprex/DESCRIPTION
/usr/lib64/R/library/reprex/INDEX
/usr/lib64/R/library/reprex/LICENSE
/usr/lib64/R/library/reprex/Meta/Rd.rds
/usr/lib64/R/library/reprex/Meta/features.rds
/usr/lib64/R/library/reprex/Meta/hsearch.rds
/usr/lib64/R/library/reprex/Meta/links.rds
/usr/lib64/R/library/reprex/Meta/nsInfo.rds
/usr/lib64/R/library/reprex/Meta/package.rds
/usr/lib64/R/library/reprex/Meta/vignette.rds
/usr/lib64/R/library/reprex/NAMESPACE
/usr/lib64/R/library/reprex/NEWS.md
/usr/lib64/R/library/reprex/R/reprex
/usr/lib64/R/library/reprex/R/reprex.rdb
/usr/lib64/R/library/reprex/R/reprex.rdx
/usr/lib64/R/library/reprex/addins/reprex.css
/usr/lib64/R/library/reprex/doc/index.html
/usr/lib64/R/library/reprex/doc/reprex-dos-and-donts.R
/usr/lib64/R/library/reprex/doc/reprex-dos-and-donts.Rmd
/usr/lib64/R/library/reprex/doc/reprex-dos-and-donts.html
/usr/lib64/R/library/reprex/help/AnIndex
/usr/lib64/R/library/reprex/help/aliases.rds
/usr/lib64/R/library/reprex/help/figures/README-viewer-screenshot.png
/usr/lib64/R/library/reprex/help/figures/help-me-help-you.png
/usr/lib64/R/library/reprex/help/figures/lifecycle-stable-brightgreen.svg
/usr/lib64/R/library/reprex/help/figures/logo.png
/usr/lib64/R/library/reprex/help/paths.rds
/usr/lib64/R/library/reprex/help/reprex.rdb
/usr/lib64/R/library/reprex/help/reprex.rdx
/usr/lib64/R/library/reprex/html/00Index.html
/usr/lib64/R/library/reprex/html/R.css
/usr/lib64/R/library/reprex/rstudio/addins.dcf
/usr/lib64/R/library/reprex/templates/BETTER_THAN_NOTHING.R
/usr/lib64/R/library/reprex/templates/REPREX.R
/usr/lib64/R/library/reprex/tests/testthat.R
/usr/lib64/R/library/reprex/tests/testthat/expressions.rds
/usr/lib64/R/library/reprex/tests/testthat/helper.R
/usr/lib64/R/library/reprex/tests/testthat/reference/srcref_reprex
/usr/lib64/R/library/reprex/tests/testthat/test-env.R
/usr/lib64/R/library/reprex/tests/testthat/test-filepaths.R
/usr/lib64/R/library/reprex/tests/testthat/test-input.R
/usr/lib64/R/library/reprex/tests/testthat/test-knitr-options.R
/usr/lib64/R/library/reprex/tests/testthat/test-optionally.R
/usr/lib64/R/library/reprex/tests/testthat/test-outfiles.R
/usr/lib64/R/library/reprex/tests/testthat/test-pandoc.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex.R
/usr/lib64/R/library/reprex/tests/testthat/test-session-info.R
/usr/lib64/R/library/reprex/tests/testthat/test-stdout-stderr.R
/usr/lib64/R/library/reprex/tests/testthat/test-stringify-expression.R
/usr/lib64/R/library/reprex/tests/testthat/test-styler.R
/usr/lib64/R/library/reprex/tests/testthat/test-tidyverse.R
/usr/lib64/R/library/reprex/tests/testthat/test-undo.R
/usr/lib64/R/library/reprex/tests/testthat/test-utils.R
/usr/lib64/R/library/reprex/tests/testthat/test-venues.R
