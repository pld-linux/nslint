Summary:	Checks DNS files for errors
Summary(pl.UTF-8):	Wyszukiwanie błędów w plikach DNS
Name:		nslint
Version:	2.1a7
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.gz
# Source0-md5:	c44a209f2c291f9cf0c5201399c3af15
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-do_not_check_for_libsnl.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nslint is a lint-like program that checks DNS files for errors. DNS or
Domain Name System generally maps names to IP addresses and e-mail
addresses in a hierarchical fashion.

Errors detected include missing trailing dots, illegal characters (RFC
1034), A records without matching PTR records and vice-versa,
duplicate names in a subnet, duplicate names for an address, names
with CNAME records (RFC 1033) missing quotes, and unknown keywords.

%description -l pl.UTF-8
nslint jest programem podobnym do linta, który wyszukuje błędy w
plikach DNS. DNS jest systemem odwzorowującym nazwy na adresy IP w
sposób hierarchiczny.

Wyszukiwane błędy to brakujące kropki kończące, nielegalne znaki (RFC
1034), rekordy A bez odpowiadających rekordów PTR (i odwrotnie),
powtórzone nazwy w podsieci, powtórzone nazwy dla adresu, nazwy z
rekordami CNAME (RFC 1033), brakujące cudzysłowy, nieznane słowa
kluczowe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/nslint
%{_mandir}/man8/*
