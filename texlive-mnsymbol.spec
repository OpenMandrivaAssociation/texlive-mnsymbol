# revision 18651
# category Package
# catalog-ctan /fonts/mnsymbol
# catalog-date 2008-08-22 15:19:59 +0200
# catalog-license pd
# catalog-version 1.4
Name:		texlive-mnsymbol
Version:	1.4
Release:	4
Summary:	Mathematical symbol font for Adobe MinionPro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/mnsymbol
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnsymbol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnsymbol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mnsymbol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MnSymbol is a symbol font family, designed to be used in
conjunction with Adobe Minion Pro (via the MinionPro package).
Almost all of LaTeX and AMS mathematical symbols are provided;
remaining coverage is available from the MinionPro font with
the MinionPro package. The fonts are available in both MetaFont
and Adobe Type 1 formats, and a comprehensive support package
is provided. While the fonts were designed to fit with Minon
Pro, the design should fit well with other renaissance or
baroque faces: indeed, it will probably work with most fonts
that are neither too wide nor too thin, for example Palatino or
Times; it is known to look good with Sabon. There is no package
designed to configure its use with any font other than Minion
Pro, but (for example) simply loading mnsymbol after mathpazo
will probably do what is needed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolA.enc
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolB.enc
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolC.enc
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolD.enc
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolE.enc
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolF.enc
%{_texmfdistdir}/fonts/enc/dvips/mnsymbol/MnSymbolS.enc
%{_texmfdistdir}/fonts/map/dvips/mnsymbol/MnSymbol.map
%{_texmfdistdir}/fonts/map/vtex/mnsymbol/MnSymbol.ali
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold10.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold12.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold5.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold6.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold7.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold8.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol-Bold9.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol10.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol12.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol5.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol6.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol7.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol8.otf
%{_texmfdistdir}/fonts/opentype/public/mnsymbol/MnSymbol9.otf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbol-Parameter.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolA9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolB9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolC9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolD9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolE9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolF9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS-Bold9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS10.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS12.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS5.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS6.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS7.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS8.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/MnSymbolS9.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Accent.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Arrows.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Base.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Delim.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Geometric.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Init.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Operators.mf
%{_texmfdistdir}/fonts/source/public/mnsymbol/Sym-Order.mf
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolA9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolB9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolC9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolD9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolE9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolF9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS-Bold9.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS10.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS12.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS5.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS6.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS7.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS8.tfm
%{_texmfdistdir}/fonts/tfm/public/mnsymbol/MnSymbolS9.tfm
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold10.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold12.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold5.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold6.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold7.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold8.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol-Bold9.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol10.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol12.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol5.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol6.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol7.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol8.pfb
%{_texmfdistdir}/fonts/type1/public/mnsymbol/MnSymbol9.pfb
%{_texmfdistdir}/tex/latex/mnsymbol/MnSymbol.sty
%doc %{_texmfdistdir}/doc/latex/mnsymbol/MnSymbol.pdf
%doc %{_texmfdistdir}/doc/latex/mnsymbol/README
#- source
%doc %{_texmfdistdir}/source/latex/mnsymbol/MnSymbol.drv
%doc %{_texmfdistdir}/source/latex/mnsymbol/MnSymbol.dtx
%doc %{_texmfdistdir}/source/latex/mnsymbol/MnSymbol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 754066
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 719051
- texlive-mnsymbol
- texlive-mnsymbol
- texlive-mnsymbol
- texlive-mnsymbol

