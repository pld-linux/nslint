Summary: Checks DNS files for errors
Name: nslint
Version: 2.0.1a1
Release: 2
Copyright: BSD
Group: Utilities/Network
Source: ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.Z
Packager: Dan E. Anderson http://www.dan.pmbc.com/
Distribution: Dan E. Anderson http://www.dan.pmbc.com/
Vendor: Dan E. Anderson http://www.dan.pmbc.com/
Buildroot: /var/tmp/nslint-root
Prefix: /usr

%description
nslint is a lint-like program that checks DNS files for errors. 
DNS or Domain Name System generally maps names to IP addresses
and e-mail addresses in a hierarchical fashion.

Errors detected include missing trailing dots, illegal characters
(RFC 1034), A records without matching PTR records and vice-versa,
duplicat names in a subnet, duplicate names for an address,
names with cname records (RFC 1033) missing quotes, and unknown keywords.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS
./configure
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin/ $RPM_BUILD_ROOT/usr/man/man8/
install -m755 -c -s nslint $RPM_BUILD_ROOT/usr/sbin
install -m644 -c nslint.8 $RPM_BUILD_ROOT/usr/man/man8

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES FILES INSTALL README VERSION
/usr/sbin/nslint
/usr/man/man8/nslint.8

%changelog 
* Tue Jun 22 1999 Dan Anderson <danx@cts.com>
- Created package
