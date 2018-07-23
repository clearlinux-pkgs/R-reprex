#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reprex
Version  : 0.2.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/reprex_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reprex_0.2.0.tar.gz
Summary  : Prepare Reproducible Example Code via the Clipboard
Group    : Development/Tools
License  : MIT
BuildRequires : R-callr
BuildRequires : R-clipr
BuildRequires : R-devtools
BuildRequires : R-markdown
BuildRequires : R-rmarkdown
BuildRequires : R-styler
BuildRequires : R-whisker
BuildRequires : clr-R-helpers

%description
small snippets of code to target formats that include both code and output.
  The goal is to encourage the sharing of small, reproducible, and runnable

%prep
%setup -q -c -n reprex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532314923

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532314923
export LANG=C
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library reprex|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
