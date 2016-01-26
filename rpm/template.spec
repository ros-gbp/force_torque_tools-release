Name:           ros-jade-force-torque-tools
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS force_torque_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/force_torque_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-force-torque-sensor-calib
Requires:       ros-jade-gravity-compensation
BuildRequires:  ros-jade-catkin

%description
Tools for gravity compensation and force-torque sensor calibration.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Jan 25 2016 Francisco Vina <fevb@kth.se> - 1.1.0-0
- Autogenerated by Bloom

* Mon Jan 25 2016 Francisco Vina <fevb@kth.se> - 1.0.2-0
- Autogenerated by Bloom

* Sun May 17 2015 Francisco Vina <fevb@kth.se> - 1.0.1-0
- Autogenerated by Bloom

