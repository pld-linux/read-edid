Summary:	Gets various useful informations from a conforming PnP monitor
Name:		read-edid
Version:	1.4.1
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://john.fremlin.de/programs/linux/read-edid/%{name}-%{version}.tar.gz
# Source0-md5:	aadc9a21ea4a1c9819757cda973372f4
Source1:	%{name}-get-edid-ppc.sh
URL:		http://john.fremlin.de/programs/linux/read-edid/index.html
#BuildRequires:	autoconf
#BuildRequires:	automake
#ExclusiveArch:	%{ix86}
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

%prep
%setup -q

%build
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
%configure
%{__make} \
%ifnarch %{ix86}
	parse-edid
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install parse-edid $RPM_BUILD_ROOT%{_bindir}/parse-edid

%ifarch %{ix86}
install get-edid $RPM_BUILD_ROOT%{_bindir}/get-edid
%endif
%ifarch ppc
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/get-edid
%endif

install get-edid.man $RPM_BUILD_ROOT%{_mandir}/man1/get-edid.1
echo ".so get-edid.1" > $RPM_BUILD_ROOT%{_mandir}/man1/parse-edid.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LRMI NEWS README
%attr(755,root,root) %{_bindir}/parse-edid
%ifarch %{ix86} ppc
%attr(755,root,root) %{_bindir}/get-edid
%endif
%{_mandir}/man1/*-edid.1*
