#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Google-Calendar
Summary:	perl(Net::Google::Calendar)
Summary(pl):	perl(Net::Google::Calendar)
Name:		perl-Net-Google-Calendar
Version:	0.2_devel
Release:	0
# note if it is "same as perl"
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}
# most of CPAN modules have generic URL (substitute pdir and pnam here)
#URL:		http://search.cpan.org/dist/%{pdir}-%{pnam}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#BuildRequires:	-
%if %{with autodeps} || %{with tests}
#BuildRequires:	perl-
#BuildRequires:	perl-
%endif
#Requires:	-
#Provides:	-
#Obsoletes:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
a

%description -l pl
b

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%patch0 -p1

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

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
# note it's mostly easier to copy unpackaged filelist here, and run adapter over the spec.
# use macros:
%{perl_vendorlib}/Net/Google/Calendar.pm
%dir %{perl_vendorlib}/Net/Google/Calendar
%{perl_vendorlib}/Net/Google/Calendar/*.pm
#%%{perl_vendorarch}/...
%{_mandir}/man3/*
