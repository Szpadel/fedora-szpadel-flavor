Name:           fish-enhanced
Version:        0.2
Release:        8%{?dist}
BuildArch:      noarch
Summary:        Szpadel's opinionated fish enhancements

License:        GPL3
URL:            https://github.com/Szpadel/fedora-szpadel-flavor

Source0:        fish-enhanced.tar.gz

Requires:       fish

%description
Szpadel's opinionated fish enhancements

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
* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-8
- rebuilt

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-7
- rebuilt

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-6
- rebuilt

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-5
- rebuilt

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-4
- rebuilt

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-3
- rebuilt

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-2
- Small issue with missing placeholder

* Sat Mar 16 2024 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.2-1
- Color prompt when connected via SSH

* Fri Nov 17 2023 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.1-3
- update pwd

* Wed Nov 15 2023 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.1-2
- rebuilt

* Wed Nov 15 2023 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.1-1
- Initial release
