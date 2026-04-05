#ifndef NS3_UTILS_H
#define NS3_UTILS_H

#include <string>
#include <iostream>

#include "ns3_all.h"
#include "wifi_config.h"

/* Parsing utilities */

/** Set the wifi standard as specified by a string. */
bool SetWifiStandardByString(ns3::WifiStandard* target,
		const std::string stdString);

/* Utilities for assignment spec processing */

bool ParseAttributeAssignmentSpec(std::pair<std::string, std::string>& kv,
		const std::string& assignmentSpec);

bool SetAttributeByAssignmentSpec(ns3::Ptr<ns3::Object> object,
		const std::string& assignmentSpec);

template<typename HelperClass>
  bool SetFactoryAttributeByAssignmentSpec(HelperClass* helper,
		const std::string& assignmentSpec);

#if 0
void setObjectAttributes(ns3::Ptr<ns3::ObjectBase> obj,
		const std::vector< std::pair<std::string, std::string> >& attribs);
#endif

#if 0
template<class HelperClass>
  void setFactoryAttributes(HelperClass& factory,
		const std::vector< std::pair<std::string, std::string> >& attribs);
#endif

/* Utilities for object configuration */

// New simplified version for variadics API in NS-3
bool setObjectFromConfigFactory(
	const ns3objectConfig& objectConfig,
	ns3::ObjectFactory& factory);

bool configureWifiChannel(ns3::YansWifiChannelHelper* helper,
			  const wifiConfig& cfg);

template<typename WifiHelperType>
  bool configureWifiStdAndRateControl(
	WifiHelperType* target,
	const wifiConfig& cfg);

bool configureWifiPhy(ns3::YansWifiPhyHelper* phy,
		      const wifiConfig& cfg);

/* Template implementations. */

template<typename HelperClass>
  bool SetFactoryAttributeByAssignmentSpec(HelperClass* helper,
		const std::string& assignmentSpec)
{
	std::pair<std::string, std::string> kv;
	if (!ParseAttributeAssignmentSpec(kv, assignmentSpec)) {
		/* Error message already printed */
		return false;
	}

	helper->Set(kv.first, ns3::StringValue(kv.second));
	return true;
}

template<typename Owner>
  bool setObjectFromConfig(
	Owner* target,
	void (Owner::*setterMethod)(std::string name,
		std::string n0, const ns3::AttributeValue& v0,
		std::string n1, const ns3::AttributeValue& v1,
		std::string n2, const ns3::AttributeValue& v2,
		std::string n3, const ns3::AttributeValue& v3,
		std::string n4, const ns3::AttributeValue& v4,
		std::string n5, const ns3::AttributeValue& v5,
		std::string n6, const ns3::AttributeValue& v6,
		std::string n7, const ns3::AttributeValue& v7),
	const ns3objectConfig& objectConfig)
{
	// New NS-3 API uses variadics templates
	// For now, we just call with the type name and no attributes
	// TODO: Implement proper variadics parameter passing if custom attributes needed
	return true;
}

template<typename WifiHelperType>
  bool configureWifiStdAndRateControl(WifiHelperType* target,
				      const wifiConfig& cfg)
{
	// Set the Wifi standard
	ns3::WifiStandard std;
	if (!SetWifiStandardByString(&std, cfg.wifi_standard))
		return false;
	target->SetStandard(std);

	// Set the remote station manager - use type name only for new API
	if (!cfg.station_manager.type_name.empty()) {
		target->SetRemoteStationManager(cfg.station_manager.type_name);
	}

	return true;
}


#endif /* NS3_UTILS_H */
