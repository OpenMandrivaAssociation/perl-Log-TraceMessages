%define	module	Log-TraceMessages
%define	name	perl-%{module}
%define	version	1.4
%define release 10

Summary:	Log::TraceMessages Perl Module
License:	GPL or Artistic
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Perl
Url:		https://www.cpan.org/
Source0:	%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-FromText
BuildArch:	noarch


%description
Log::TraceMessages

This module is a better way of putting 'hello there' trace messages in
your code.  It lets you turn tracing on and off without commenting out
trace statements, and provides other useful things like HTML-ified
trace messages for CGI scripts and an easy way to trace out data
structures using Data::Dumper.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Log/TraceMessages.pm
%{perl_vendorlib}/auto/Log/TraceMessages/autosplit.ix
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4-8mdv2010.0
+ Revision: 430483
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-7mdv2009.0
+ Revision: 257671
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-6mdv2009.0
+ Revision: 245709
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.4-4mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.4-4mdv2008.0
+ Revision: 86524
- rebuild


* Sat Sep 02 2006 Stefan van der Eijk <stefan@mandriva.org> 1.4-3mdk
- yearly rebuild
- add %%check section

* Thu Jun 02 2005 Stefan van der Eijk <stefan@eijk.nu> 1.4-2mdk
- %%mkrel
- yearly rebuild

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4-1mdk
- 1.4
- clean %%description
- cosmetics

* Sat Nov 29 2003 Stefan van der Eijk <stefan@eijk.nu> 1.3-1mdk
- 1.3

