%include	/usr/lib/rpm/macros.perl
%define	pdir	Digest
%define	pnam	SHA1
Summary:	Perl Digest-SHA1 module
Summary(pl):	Modu³ Perla Digest-SHA1
Name:		perl-Digest-SHA1
Version:	2.01
Release:	3
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

%description -l pl
Modu³ Digest::SHA1 pozwala u¿ywaæ algorytmu skrótu NIST SHA-1 z
programów w Perlu. Algorytm pobiera z wej¶cia wiadomo¶æ dowolnej
d³ugo¶ci, a na wyj¶ciu produkuje 160-bitowy "odcisk palca" lub "skrót
wiadomo¶ci" z wej¶cia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{perl_archlib}

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

gzip -9nf README Changes 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz fip180*
%{perl_sitearch}/Digest
%dir %{perl_sitearch}/auto/Digest/*
%{perl_sitearch}/auto/Digest/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/*/*.so

%{_mandir}/man3/*
