#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA1
Summary:	Digest::SHA1 - interface to the SHA-1 algorithm
Summary(pl.UTF-8):   Digest::SHA1 - interfejs do algorytmu SHA-1
Name:		perl-Digest-SHA1
Version:	2.11
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2449bfe21d6589c96eebf94dae24df6b
Patch0:		%{name}-reset.patch
URL:		http://search.cpan.org/dist/Digest-SHA1/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%patch0 -p1

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
