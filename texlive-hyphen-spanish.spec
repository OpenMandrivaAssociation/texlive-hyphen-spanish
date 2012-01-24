# revision 23092
# category TLCore
# catalog-ctan /language/spanish/hyphen/base
# catalog-date 2009-08-01 23:35:18 +0200
# catalog-license lppl
# catalog-version 4.5
Name:		texlive-hyphen-spanish
Version:	4.5
Release:	3
Summary:	Spanish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/spanish/hyphen/base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-spanish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Spanish in T1/EC and UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-spanish
%_texmf_language_def_d/hyphen-spanish
%_texmf_language_lua_d/hyphen-spanish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-spanish <<EOF
\%% from hyphen-spanish:
spanish loadhyph-es.tex
=espanol
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-spanish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-spanish <<EOF
\%% from hyphen-spanish:
\addlanguage{spanish}{loadhyph-es.tex}{}{2}{2}
\addlanguage{espanol}{loadhyph-es.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-spanish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-spanish <<EOF
-- from hyphen-spanish:
	['spanish'] = {
		loader = 'loadhyph-es.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'espanol' },
		patterns = 'hyph-es.pat.txt',
		hyphenation = '',
	},
EOF
