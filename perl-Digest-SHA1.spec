#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA1
Summary:	Perl Digest::SHA1 module
Summary(pl):	Modu� Perla Digest::SHA1
Summary(pt_BR):	M�dulo Digest::SHA1
Name:		perl-Digest-SHA1
Version:	2.07
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc6f30d34f9c972dcc0a767386e4b6fe
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::SHA1 module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

%description -l pl
Modu� Digest::SHA1 pozwala u�ywa� algorytmu skr�tu NIST SHA-1 z
program�w w Perlu. Algorytm pobiera z wej�cia wiadomo�� dowolnej
d�ugo�ci, a na wyj�ciu produkuje 160-bitowy "odcisk palca" lub "skr�t
wiadomo�ci" z wej�cia.

%description -l pt_BR
Este m�dulos Perl permite a utiliza��o do algoritmo de digest de
mensagens NIST SHA-1 em programas Perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes fip180*
%{perl_vendorarch}/Digest/*
%dir %{perl_vendorarch}/auto/Digest/*
%{perl_vendorarch}/auto/Digest/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/*/*.so

%{_mandir}/man3/*
