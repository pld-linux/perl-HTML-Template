#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Template
Summary:	HTML::Template - Perl module to use HTML templates from CGI scripts
Summary(pl):	HTML::Template - modu� Perla do obs�ugi szablon�w HTML w skryptach CGI
Name:		perl-HTML-Template
Version:	2.6
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dbd1c0c23fe323123deb9212c82a6f2d
URL:		http://html-template.sourceforge.net/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
%if %{with tests}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-IPC-SharedCache
BuildRequires:	perl-Storable
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts make using HTML templates simple and natural.

It extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
<TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF> and <TMPL_ELSE>.  The file written
with HTML and these new tags is called a template.  It is usually saved
separate from your script - possibly even created by someone else!

Using this module you fill in the values for the variables, loops and
branches declared in the template.  This allows you to seperate design -
the HTML - from the data, which you generate in the Perl script.

%description -l pl
HTML::Template jest modu�em pozwalaj�cym na wykorzystywanie szablon�w
HTML (i nie tylko) w skryptach CGI (a tak�e w dowolnym innym
oprogramowaniu przy tworzeniu kt�rego zachodzi potrzeba rozdzielenia
programu od wygl�du danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}/%{pnam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ANNOUNCE FAQ templates scripts
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*