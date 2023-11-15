Name:           fish-enhanced
Version:        0.1
Release:        1%{?dist}
BuildArch:      noarch
Summary:        Szpadel's opinionated fish enhancments

License:        GPL3
URL:            https://github.com/Szpadel/fedora-szpadel-flavor

Source0:        fish-enhanced.tar.gz

%description
Szpadel's opinionated fish enhancments

%prep
%autosetup -n files

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/etc/fish/functions/
mkdir -p %{buildroot}/etc/fish/conf.d/
cp -r functions/* %{buildroot}/etc/fish/functions/
cp -r conf.d/* %{buildroot}/etc/fish/conf.d/


%files
/etc/fish/functions/*
/etc/fish/conf.d/*


%changelog
* Wed Nov 15 2023 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.1-1
- Initial release
