Name:           bash-enhanced
Version:        0.1
Release:        1%{?dist}
Summary:        Szpadel's opinionated bash enhancments

License:        GPL3
URL:            

BuildRequires:  
Requires:       hstr

Source0:        %{expand:%%(pwd)}

%description
Szpadel's opinionated bash enhancments

%prep


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/etc/profile.d/
cp ${SOURCEURL0}/profile.d/*.sh %{buildroot}/etc/profile.d/


%files
/etc/profile.d/bash_color.sh
/etc/profile.d/bash_spell.sh
/etc/profile.d/hstr.sh
/etc/profile.d/neovim.sh
/etc/profile.d/yarnpkg.sh


%changelog
* Mon Jan 27 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl>
- 
