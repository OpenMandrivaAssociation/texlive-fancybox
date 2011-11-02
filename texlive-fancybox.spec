Name:		texlive-fancybox
Version:	1.4
Release:	1
Summary:	Variants of \fbox and other games with boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancybox
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancybox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancybox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides variants of \fbox: \shadowbox, \doublebox, \ovalbox,
\Ovalbox, with helpful tools for using box macros and flexible
verbatim macros. You can box mathematics, floats, center,
flushleft, and flushright, lists, and pages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
