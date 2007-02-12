#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Google-Calendar
Summary:	Net::Google::Calendar - programmatic access to Google's Calendar API
Summary(pl.UTF-8):   Net::Google::Calendar - dostęp do API Google Calendar
Name:		perl-Net-Google-Calendar
Version:	0.2_devel
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/Net-Google-Calendar/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interact with Google's new calendar.

%description -l pl.UTF-8
Moduł do współpracy z nowym kalendarzem Google.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Readme TODO USAGE
%{perl_vendorlib}/Net/Google/Calendar.pm
%dir %{perl_vendorlib}/Net/Google/Calendar
%{perl_vendorlib}/Net/Google/Calendar/*.pm
%{_mandir}/man3/*
