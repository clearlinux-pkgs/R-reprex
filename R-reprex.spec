#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reprex
Version  : 2.0.2
Release  : 56
URL      : https://cran.r-project.org/src/contrib/reprex_2.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reprex_2.0.2.tar.gz
Summary  : Prepare Reproducible Example Code via the Clipboard
Group    : Development/Tools
License  : MIT
Requires: R-callr
Requires: R-cli
Requires: R-clipr
Requires: R-fs
Requires: R-glue
Requires: R-knitr
Requires: R-lifecycle
Requires: R-rlang
Requires: R-rmarkdown
Requires: R-rstudioapi
Requires: R-withr
BuildRequires : R-callr
BuildRequires : R-cli
BuildRequires : R-clipr
BuildRequires : R-fs
BuildRequires : R-glue
BuildRequires : R-knitr
BuildRequires : R-lifecycle
BuildRequires : R-rlang
BuildRequires : R-rmarkdown
BuildRequires : R-rstudioapi
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
render small snippets of code to target formats that include both code
    and output.  The goal is to encourage the sharing of small,
    reproducible, and runnable examples on code-oriented websites, such as

%prep
%setup -q -n reprex
cd %{_builddir}/reprex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660749532

%install
export SOURCE_DATE_EPOCH=1660749532
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/reprex/R/sysdata.rdb
/usr/lib64/R/library/reprex/R/sysdata.rdx
/usr/lib64/R/library/reprex/WORDLIST
/usr/lib64/R/library/reprex/addins/reprex.css
/usr/lib64/R/library/reprex/doc/index.html
/usr/lib64/R/library/reprex/doc/reprex-dos-and-donts.R
/usr/lib64/R/library/reprex/doc/reprex-dos-and-donts.Rmd
/usr/lib64/R/library/reprex/doc/reprex-dos-and-donts.html
/usr/lib64/R/library/reprex/help/AnIndex
/usr/lib64/R/library/reprex/help/aliases.rds
/usr/lib64/R/library/reprex/help/figures/README-viewer-screenshot.png
/usr/lib64/R/library/reprex/help/figures/help-me-help-you.png
/usr/lib64/R/library/reprex/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/reprex/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/reprex/help/figures/logo.png
/usr/lib64/R/library/reprex/help/paths.rds
/usr/lib64/R/library/reprex/help/reprex.rdb
/usr/lib64/R/library/reprex/help/reprex.rdx
/usr/lib64/R/library/reprex/html/00Index.html
/usr/lib64/R/library/reprex/html/R.css
/usr/lib64/R/library/reprex/rmarkdown/templates/reprex-featureful/skeleton/skeleton.Rmd
/usr/lib64/R/library/reprex/rmarkdown/templates/reprex-featureful/template.yaml
/usr/lib64/R/library/reprex/rmarkdown/templates/reprex-minimal/skeleton/skeleton.Rmd
/usr/lib64/R/library/reprex/rmarkdown/templates/reprex-minimal/template.yaml
/usr/lib64/R/library/reprex/rstudio/addins.dcf
/usr/lib64/R/library/reprex/templates/BETTER_THAN_NOTHING.R
/usr/lib64/R/library/reprex/tests/spelling.R
/usr/lib64/R/library/reprex/tests/testthat.R
/usr/lib64/R/library/reprex/tests/testthat/_snaps/input.md
/usr/lib64/R/library/reprex/tests/testthat/_snaps/reprex.md
/usr/lib64/R/library/reprex/tests/testthat/_snaps/reprex_document.md
/usr/lib64/R/library/reprex/tests/testthat/_snaps/rprofile.md
/usr/lib64/R/library/reprex/tests/testthat/_snaps/utils-clipboard.md
/usr/lib64/R/library/reprex/tests/testthat/_snaps/utils-io.md
/usr/lib64/R/library/reprex/tests/testthat/_snaps/utils-ui.md
/usr/lib64/R/library/reprex/tests/testthat/expressions.rds
/usr/lib64/R/library/reprex/tests/testthat/fixtures/a-reprex-document.Rmd
/usr/lib64/R/library/reprex/tests/testthat/helper.R
/usr/lib64/R/library/reprex/tests/testthat/setup.R
/usr/lib64/R/library/reprex/tests/testthat/test-env.R
/usr/lib64/R/library/reprex/tests/testthat/test-input.R
/usr/lib64/R/library/reprex/tests/testthat/test-knitr-options.R
/usr/lib64/R/library/reprex/tests/testthat/test-outfiles.R
/usr/lib64/R/library/reprex/tests/testthat/test-pandoc.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex-addin.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex-options.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex-undo.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex_document.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex_impl.R
/usr/lib64/R/library/reprex/tests/testthat/test-reprex_render.R
/usr/lib64/R/library/reprex/tests/testthat/test-rprofile.R
/usr/lib64/R/library/reprex/tests/testthat/test-session-info.R
/usr/lib64/R/library/reprex/tests/testthat/test-stdout-stderr.R
/usr/lib64/R/library/reprex/tests/testthat/test-stringify_expression.R
/usr/lib64/R/library/reprex/tests/testthat/test-utf8.R
/usr/lib64/R/library/reprex/tests/testthat/test-utils-clipboard.R
/usr/lib64/R/library/reprex/tests/testthat/test-utils-io.R
/usr/lib64/R/library/reprex/tests/testthat/test-utils-ui.R
/usr/lib64/R/library/reprex/tests/testthat/test-utils.R
/usr/lib64/R/library/reprex/tests/testthat/test-venues.R
