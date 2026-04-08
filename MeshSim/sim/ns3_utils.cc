#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#include "ns3_utils.h"

using namespace ns3;
using namespace std;

WifiStandard GetWifiStandardFromString(const string stdString)
{
	// Modern NS-3 WifiStandard enum - simplified for core standards
	if (stdString == "a" || stdString == "802.11a")
		return WIFI_STANDARD_80211a;
	else if (stdString == "b" || stdString == "802.11b")
		return WIFI_STANDARD_80211b;
	else if (stdString == "g" || stdString == "802.11g")
		return WIFI_STANDARD_80211g;
	// Map 11n/ax variants to 802.11ac (modern replacement)
	else if (stdString == "n2.4" || stdString == "802.11n2.4" || 
	         stdString == "n5" || stdString == "802.11n5" ||
	         stdString == "ac" || stdString == "802.11ac" ||
	         stdString == "ax2.4" || stdString == "802.11ax2.4" ||
	         stdString == "ax5" || stdString == "802.11ax5")
		return WIFI_STANDARD_80211ac;
	else {
		cerr << "Warning: Wifi standard \"" << stdString
		     << "\" unknown. Using 802.11g as default.\n";
		return WIFI_STANDARD_80211g;
	}
}

bool ParseAttributeAssignmentSpec(pair<string, string>& kv,
			     const string& assignmentSpec)
{
	string::const_iterator
	  x = find(assignmentSpec.begin(), assignmentSpec.end(), '=');
	if (x == assignmentSpec.end()) {
		cerr << "Error:  Malformed attribute assignment spec \""
		     << assignmentSpec << "\".\n";
		return false;
	}

	kv.first = string(assignmentSpec.begin(), x);
	kv.second = string(x + 1, assignmentSpec.end());
	return true;
}

bool SetAttributeByAssignmentSpec(Ptr<Object> object,
			     const string& assignmentSpec)
{
	pair<string, string> kv;
	if (!ParseAttributeAssignmentSpec(kv, assignmentSpec)) {
		/* Error message already printed */
		return false;
	}

	object->SetAttribute(kv.first, StringValue(kv.second));
	return true;
}

bool configureWifiChannel(YansWifiChannelHelper* helper,
				 const wifiConfig& cfg)
{
	// Always set propagation delay and loss models explicitly
	// (even for default channel configuration)
	
	// Set delay model
	if (cfg.delay_model.type_name != "") {
		helper->SetPropagationDelay(cfg.delay_model.type_name);
	} else {
		helper->SetPropagationDelay("ns3::ConstantSpeedPropagationDelayModel");
	}

	// Apply propagation loss models
	if (!cfg.loss_model.empty()) {
		for (int i = 0; i < int(cfg.loss_model.size()); ++i) {
			if (cfg.loss_model[i].type_name == "@matrix") {
				cerr << "Error:  @matrix loss not implemented.\n";
				return false;
			} else if (cfg.loss_model[i].type_name != "") {
				helper->AddPropagationLoss(cfg.loss_model[i].type_name);
			}
		}
	} else {
		// Default loss model if none specified
		helper->AddPropagationLoss("ns3::FriisPropagationLossModel");
	}
	
	return true;
}

bool configureWifiPhy(ns3::YansWifiPhyHelper* phy,
		      const wifiConfig& cfg)
{
	for (const auto& a : cfg.phy_attribs) {
		if (!SetFactoryAttributeByAssignmentSpec(phy, a)) {
			return false;
		}
	}

	return true;
}
