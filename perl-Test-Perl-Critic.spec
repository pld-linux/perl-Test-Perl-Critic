#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Perl-Critic
Summary:	Test::Perl::Critic - Use Perl::Critic in test programs
Summary(pl.UTF-8):	Test::Perl::Critic - użycie Perl::Critic w programach testowych
Name:		perl-Test-Perl-Critic
Version:	1.03
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b10da607ed6c6c07eba99e48ce77d88a
URL:		http://search.cpan.org/dist/Test-Perl-Critic/
BuildRequires:	perl-Module-Build >= 0.40
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MCE >= 1.520
BuildRequires:	perl-Perl-Critic >= 1.105
BuildRequires:	perl-Test-Simple
%endif
Requires:	perl-MCE >= 1.520
Requires:	perl-Perl-Critic >= 1.105
Requires:	perl-dirs >= 4-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Perl::Critic wraps the Perl::Critic engine in a convenient
subroutine suitable for test programs written using the Test::More
framework. This makes it easy to integrate coding-standards
enforcement into the build process. For ultimate convenience (at the
expense of some flexibility), see the criticism pragma.

%description -l pl.UTF-8
Test::Perl::Critic obudowuje silnik Perl::Critic w wygodną procedurę
pasującą do programów testowych pisanych z użyciem szkieletu
Test::More. Ułatwia to integrację wymuszania standardów kodowania w
proces budowania. Dla ostatecznej wygody (kosztem części
elastyczności) użyć pragma criticism.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test/Perl/Critic.pm
%{_mandir}/man3/Test::Perl::Critic.3*
