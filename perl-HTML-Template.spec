#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Template
Summary:	HTML::Template - Perl module to use HTML templates from CGI scripts
Summary(pl.UTF-8):	HTML::Template - moduł Perla do obsługi szablonów HTML w skryptach CGI
Name:		perl-HTML-Template
Version:	2.95
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f08e9631af52e6a5f6e4648b89265fe
URL:		https://github.com/mpeters/html-template/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IPC-SharedCache
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts make using HTML templates simple and natural.

It extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>. The file
written with HTML and these new tags is called a template. It is
usually saved separate from your script - possibly even created by
someone else!

Using this module you fill in the values for the variables, loops and
branches declared in the template. This allows you to seperate design
- the HTML - from the data, which you generate in the Perl script.

%description -l pl.UTF-8
Ten moduł próbuje uczynić wykorzystywanie szablonów HTML prostym i
naturalnym.

Rozszerza standardowy HTML o kilka znaczników HTML-opodobnych:
<TMPL_VAR>, <TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> oraz <TMPL_ELSE>.
Plik napisany w HTML-u z użyciem tych nowych znaczników nazywa się
szablonem. Zwykle jest oddzielony od skryptu - a nawet tworzony przez
kogoś innego.

Przy użyciu tego modułu wypełnia się wartościami zmienne, pętle oraz
warunki zadeklarowane w szablonie. Pozwala to oddzielić projekt (HTML)
od danych generowanych w skrypcie perlowym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# just docs
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/Template/FAQ.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README templates scripts
%{perl_vendorlib}/HTML/Template.pm
%dir %{perl_vendorlib}/HTML/Template
%{_mandir}/man3/HTML::Template.3pm*
%{_mandir}/man3/HTML::Template::FAQ.3pm*
