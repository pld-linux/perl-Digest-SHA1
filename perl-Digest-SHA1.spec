#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA1
Summary:	Digest::SHA1 - interface to the SHA-1 algorithm
Summary(pl):	Digest::SHA1 - interfejs do algorytmu SHA-1
Name:		perl-Digest-SHA1
Version:	2.10
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4497a499b7c28ddd540a8caab412c6d7
Patch0:		%{name}-reset.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::SHA1 Perl module allows you to use the NIST SHA-1 message
digest algorithm from within Perl programs.  The algorithm takes as
input a message of arbitrary length and produces as output a 160-bit
"fingerprint" or "message digest" of the input.

%description -l pl
Modu³ Perla  Digest::SHA1 pozwala u¿ywaæ algorytmu skrótu NIST SHA-1 z
programów w Perlu. Algorytm pobiera z wej¶cia wiadomo¶æ dowolnej
d³ugo¶ci, a na wyj¶ciu produkuje 160-bitowy "odcisk palca" lub "skrót
wiadomo¶ci" z wej¶cia.

%description -l pt_BR
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
