Name:           ros-indigo-summit-x-control
Version:        1.0.8
Release:        0%{?dist}
Summary:        ROS summit_x_control package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/RobotnikAutomation/summit_x_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-ros-control
Requires:       ros-indigo-ros-controllers
Requires:       ros-indigo-summit-x-description
Requires:       ros-indigo-summit-xl-pad
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-robot-state-publisher
BuildRequires:  ros-indigo-ros-control
BuildRequires:  ros-indigo-ros-controllers
BuildRequires:  ros-indigo-summit-x-description
BuildRequires:  ros-indigo-summit-xl-pad

%description
This package contains the launch files that load the required controller
interfaces for simulation in Gazebo.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Aug 26 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.8-0
- Autogenerated by Bloom

* Wed Aug 24 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jul 15 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.5-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.4-1
- Autogenerated by Bloom

* Mon Jul 11 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.4-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.3-0
- Autogenerated by Bloom

* Mon Jul 11 2016 Román Navarro <rnavarro@robotnik.es> - 1.0.2-0
- Autogenerated by Bloom

* Fri Jul 08 2016 Robotnik <info@robotnik.es> - 1.0.1-0
- Autogenerated by Bloom

