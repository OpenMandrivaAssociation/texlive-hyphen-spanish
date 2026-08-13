%global tl_name hyphen-spanish
%global tl_revision 78069
%global tl_version 5.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-spanish:
spanish loadhyph-es.tex
=espanol
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-spanish:
\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}
\addlanguage{espanol}{loadhyph-es.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-spanish:
['spanish'] = {
	loader = 'loadhyph-es.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = { 'espanol' },
	patterns = 'hyph-es.pat.txt',
},
TL_HYPHEN_EOF
