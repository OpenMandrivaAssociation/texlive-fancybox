%global tl_name fancybox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Variants of \fbox and other games with boxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fancybox
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancybox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fancybox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides variants of \fbox: \shadowbox, \doublebox, \ovalbox, \Ovalbox,
with helpful tools for using box macros and flexible verbatim macros.
You can box mathematics, floats, center, flushleft, and flushright,
lists, and pages.

