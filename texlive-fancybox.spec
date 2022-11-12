Name:		texlive-fancybox
Version:	18304
Release:	1
Summary:	Variants of \fbox and other games with boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancybox
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancybox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancybox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides variants of \fbox: \shadowbox, \doublebox, \ovalbox,
\Ovalbox, with helpful tools for using box macros and flexible
verbatim macros. You can box mathematics, floats, center,
flushleft, and flushright, lists, and pages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fancybox/fancybox.sty
%doc %{_texmfdistdir}/doc/latex/fancybox/Changes
%doc %{_texmfdistdir}/doc/latex/fancybox/Makefile
%doc %{_texmfdistdir}/doc/latex/fancybox/README
%doc %{_texmfdistdir}/doc/latex/fancybox/fancybox-doc.pdf
%doc %{_texmfdistdir}/doc/latex/fancybox/fancybox-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
