%define use_ccache        1
%define ccachedir        ~/.ccache-OOo%{mdvsuffix}%{?_with_ccache: %global use_ccache 1}%{?_without_ccache: %global use_ccache 0}
%define                       _enable_debug_packages %{nil}
%define                        debug_package          %{nil}
%define                        distsuffix mdv
%define dont_strip 1

Vendor:         Sergey Zhemoitel <http://djam.spb.ru>
Packager:       Sergey Zhemoitel <djam5@ya.ru>
Name: 		omnitux-light
Version: 	1.2.0
Release: 	%mkrel 1
Summary: 	Educational activities based on multimedia elements.
Group:   	Educational
License: 	GPLv2
URL:     	http://omnitux.sourceforge.net/
Source:  	%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root
Requires: 	pygame, pygtk2.0, pygtk2.0-libglade


%description
Educational activities based on multimedia elements.
  
 Types of activities:
  
  * associations,
  * items to place on a map or a schema,
  * counting activities,
  * puzzles,
  * card faces to remember,
  * find differences between two pictures,
  * ...
   
 Activities are available in German, English, French, Polish and Portuguese. 

%prep
%setup -q -n %{name}

%install

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/applications


cp -r ./* %{buildroot}%{_datadir}/%{name}/
cp omnitux-light.sh %{buildroot}%{_bindir}/
cp omnitux-light.desktop %{buildroot}%{_datadir}/applications/





chmod 0755 $RPM_BUILD_ROOT%{_bindir}/omnitux-light.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc LICENSE.txt README.txt
%{_bindir}/omnitux-light.sh
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*

