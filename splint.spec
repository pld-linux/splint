%include        /usr/lib/rpm/macros.perl
Summary:	A tool for statically checking C programs
Summary(pl):	Narzêdzie do statycznego sprawdzania programów w C
Name:		splint
Version:	3.0.1.5
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	%{name}-%{version}.src.tgz
URL:		http://www.splint.org
Obsoletes:	lclint
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Splint is a tool for statically checking C programs for security
vulnerabilities and common programming mistakes. With minimal effort,
Splint can be used as a better lint(1). If additional effort is
invested adding annotations to programs, Splint can perform stronger
checks than can be done by any standard lint.

%description -l pl
Splint jest narzêdziem do statycznego sprawdzania programów w C w
zakresie naruszenia bezpieczeñstwa i popularnych b³edów
programistycznych. Z ma³ym wysi³kiem SPlint mo¿e byæ u¿ywany jako
lepszy lint(1). Przy dodatkowym wk³adzie pracy w dodawanie komentarzy
do programów Splint mo¿e wykonaæ silniejsz± kontrolê ni¿ standardowy
lint.

%prep
%setup  -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install doc/splint.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/splint
%{_datadir}/splint
%{_mandir}/man*/*
