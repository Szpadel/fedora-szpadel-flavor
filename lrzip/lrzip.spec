Name: lrzip
Version: 0.8.14
Release: 1%{?dist}

Summary: Long Range ZIP or Lzma RZIP
License: GPLv2+
Group: Applications/File

Url: https://github.com/pete4abw/lrzip-next
Source0: https://github.com/pete4abw/lrzip-next/archive/v%{version}.tar.gz

BuildRequires: doxygen gcc-c++ lzo-devel perl-Pod-Parser zlib-devel coreutils make autoconf automake libtool bzip2-devel

%description
This is a compression program optimised for large files. The larger the file
and the more memory you have, the better the compression advantage this will
provide, especially once the files are larger than 100MB. The advantage can
be chosen to be either size (much smaller than bzip2) or speed (much faster
than bzip2).

%package libs
Summary: Long Range ZIP library
Group: System Environment/Libraries

%description libs
Dynamic library implementing Long Range ZIP or Lzma RZIP algorithm and archive
format.

%package devel
Summary:  Development files for Long Range ZIP library
Group:  Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Files needed to develop application using Long Range ZIP library.


%package static
Summary:        Static Long Range ZIP library
Group:          Development/Libraries
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static library implementing Long Range ZIP or Lzma RZIP algorithm and archive
format.


%prep
%autosetup -n lrzip-next-%{version}

%build
./autogen.sh
%configure --enable-shared --enable-static --disable-static-bin --disable-silent-rules
%make_build

%install
%makeinstall

install -pDm644 Lrzip.h %buildroot%_includedir/Lrzip.h
find $RPM_BUILD_ROOT -name '*.la' -exec rm {} +

%check
./lrzip -z COPYING
./lrzip -i COPYING.lrz
./lrzip -d -o COPYING.new COPYING.lrz
cmp COPYING COPYING.new
rm COPYING.new


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%doc README.md README-NOT-BACKWARD-COMPATIBLE WHATS-NEW doc/lrzip.conf.example
%_bindir/*
%_mandir/man1/*.1.gz
%_mandir/man5/*.5.gz
%exclude %_docdir/lrzip

%files libs
%doc COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc decompress_demo.c liblrzip_demo.c
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files static
%{_libdir}/lib%{name}.a

%changelog
* Sat Oct 31 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.725-1
- Update to fork of pete4abw

* Mon Jan 27 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl> - 0.631-1
- rebuilt
