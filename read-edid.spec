Summary:	Gets various useful informations from a conforming PnP monitor
Summary(pl.UTF-8):	Pobieranie różnych przydatnych informacji z monitora zgodnego z PnP
Name:		read-edid
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://polypux.org/projects/read-edid/%{name}-%{version}.tar.gz
# Source0-md5:	586e7fa1167773b27f4e505edc93274b
URL:		http://polypux.org/projects/read-edid/
BuildRequires:	libx86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hardware information-gathering tool for VESA PnP monitors read-edid
consists of two tools:

get-edid uses a VESA VBE 2 interrupt service routine request to read a
128 byte EDID version 1 structure from your graphics card, which
retrieves this information from the monitor via the Data Display
Channel (DDC).

parse-edid parses this data structure and outputs data suitable for
inclusion into the XFree86 or X.org configuration file.

get-edid uses architecture-specific methods for querying the video
hardware (real-mode x86 instructions on i386, Open Firmware device
tree parsing on PowerMac) and is therefore only available for i386 and
powerpc architectures.

%description -l pl.UTF-8
read-edid to narzędzie do zbierania informacji dotyczących sprzętu dla
monitorów VESA PnP, składające się z dwóch programów:

get-edid używa żądania funkcji przerwania VESA VBE 2 do odczytu
128-bajtowej struktury EDID w wersji 1 od karty graficznej, która
pobiera te informacje z monitora poprzez DDC (Data Display Channel).

parse-edid analizuje tę strukturę danych i wypisuje dane nadające się
do wstawienia do pliku konfiguracyjnego XFree86 lub X.org.

get-edit używa specyficznych dla architektury metod odpytywania karty
graficznej (instrukcji w trybie rzeczywistym x86 na i386, analizy
drzewa urządzeń OpenFirmware na PowerMacu), więc jest dostępne tylko
dla architektur i386 i powerpc.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/parse-edid
%attr(755,root,root) %{_sbindir}/get-edid
%{_mandir}/man1/*-edid.1*
