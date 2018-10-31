Name:		texlive-hyphen-spanish
Version:	20180303
Release:	2
Summary:	Spanish hyphenation patterns
Group:		Publishing
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
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-spanish
%_texmf_language_def_d/hyphen-spanish
%_texmf_language_lua_d/hyphen-spanish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

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


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.5-4
+ Revision: 804814
- Update to latest release.

* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.5-3
+ Revision: 767595
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.5-2
+ Revision: 759939
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.5-1
+ Revision: 718681
- texlive-hyphen-spanish
- texlive-hyphen-spanish
- texlive-hyphen-spanish
- texlive-hyphen-spanish

