Summary:	Checks DNS files for errors
Name:		nslint
Version:	2.0.1a1
Release:	3
Copyright:	BSD
Group:		Utilities/Network
Source:		ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.Z
Patch:		nslint-makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install install-man DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/nslint
%{_mandir}/man8/*
