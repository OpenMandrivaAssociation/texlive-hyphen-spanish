%global tl_name hyphen-spanish
%global tl_revision 78069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.0
Release:	%{tl_revision}.1
Summary:	Spanish hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/spanish/hyphen-spanish
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-spanish.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-spanish.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-spanish.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.

