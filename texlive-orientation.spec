Name:		texlive-orientation
Version:	57390
Release:	2
Summary:	Set page orientation with dvips/Ghostscript (ps2pdf)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/orientation
License:	cc0
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orientation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/orientation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for manual (per-page and
per-document) orientation of pages in a PDF created with
dvips/Ghostscript (ps2pdf). For future versions it is planned
to add support for other drivers, allowing for PDF orientation
to be set in (x)dvipdfmx and pdfmode pdfTeX using the same
commands from the user perspective.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/orientation
%doc %{_texmfdistdir}/doc/latex/orientation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
