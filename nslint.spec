Summary:	Checks DNS files for errors
Summary(pl):	Wyszukiwanie b��d�w w plikach DNS
Name:		nslint
Version:	2.1a3
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	ftp://ftp.ee.lbl.gov/%{name}-%{version}.tar.gz
# Source0-md5:	87f78dd8680a4abbc480d814172a468e
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

%description -l pl
nslint jest programem podobnym do linta, kt�ry wyszukuje b��dy w
plikach DNS. DNS jest systemem odwzorowuj�cym nazwy na adresy IP w
spos�b hierarchiczny.

Wyszukiwane b��dy to brakuj�ce kropki ko�cz�ce, nielegalne znaki (RFC
1034), rekordy A bez odpowiadaj�cych rekord�w PTR (i odwrotnie),
powt�rzone nazwy w podsieci, powt�rzone nazwy dla adresu, nazwy z
rekordami CNAME (RFC 1033), brakuj�ce cudzys�owy, nieznane s�owa
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
