%global tl_name mnsymbol
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Mathematical symbol font for Adobe MinionPro
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mnsymbol
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnsymbol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnsymbol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mnsymbol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MnSymbol is a symbol font family, designed to be used in conjunction
with Adobe Minion Pro (via the MinionPro package). Almost all of LaTeX
and AMS mathematical symbols are provided; remaining coverage is
available from the MinionPro font with the MinionPro package. The fonts
are available both as Metafont source and as Adobe Type 1 format, and a
comprehensive support package is provided. While the fonts were designed
to fit with Minon Pro, the design should fit well with other renaissance
or baroque faces: indeed, it will probably work with most fonts that are
neither too wide nor too thin, for example Palatino or Times; it is
known to look good with Sabon. There is no package designed to configure
its use with any font other than Minion Pro, but (for example) simply
loading mnsymbol after mathpazo will probably do what is needed.

