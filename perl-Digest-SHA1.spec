#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Digest
%define		pnam	SHA1
Summary:	Digest::SHA1 - interface to the SHA-1 algorithm
Summary(pl.UTF-8):	Digest::SHA1 - interfejs do algorytmu SHA-1
Name:		perl-Digest-SHA1
Version:	2.13
Release:	18
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bd22388f268434f2b24f64e28bf1aa35
Patch0:		%{name}-reset.patch
URL:		https://metacpan.org/dist/Digest-SHA1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::SHA1 Perl module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs.  The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

%description -l pl.UTF-8
Moduł Perla Digest::SHA1 pozwala używać algorytmu skrótu NIST SHA-1 z
programów w Perlu. Algorytm pobiera z wejścia wiadomość dowolnej
długości, a na wyjściu produkuje 160-bitowy "odcisk palca" lub "skrót
wiadomości" z wejścia.

%description -l pt_BR.UTF-8
Este módulos Perl permite a utilização do algoritmo de digest de
mensagens NIST SHA-1 em programas Perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README fip180-1.{gif,html}
%{perl_vendorarch}/Digest/SHA1.pm
%dir %{perl_vendorarch}/auto/Digest/SHA1
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/SHA1/SHA1.so
%{_mandir}/man3/Digest::SHA1.3pm*
