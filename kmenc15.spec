Summary:	Advanced Qt/KDE MEncoder frontend
Name:		kmenc15
Version:	0.03
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kmenc15/%{name}-%{version}.tar.bz2
# Source0-md5:	986ae4b4b9d96a373af0541c93296769
URL:		http://kmenc15.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.3
Requires:	mplayer >= 1.0-0.pre5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kmenc15 is an advanced Qt/KDE MEncoder frontend, generally designed to be 
a VirtualDub replacement for Linux. It is most useful for editing and 
encoding large high quality AVIs capped from TV. It allows cutting and 
merging at exact frames, applying any MPlayer/MEncoder filter, with preview.

%prep
%setup -q

%build
%{__make} \
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
