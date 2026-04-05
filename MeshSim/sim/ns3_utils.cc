#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#include "ns3_utils.h"

using namespace ns3;
using namespace std;

bool SetWifiStandardByString(WifiStandard* target,
			const string stdString)
{
	if (stdString == "a" || stdString == "802.11a")
		*target = WIFI_STANDARD_80211a;
	else if (stdString == "b" || stdString == "802.11b")
		*target = WIFI_STANDARD_80211b;
	else if (stdString == "g" || stdString == "802.11g")
		*target = WIFI_STANDARD_80211g;
	else if (stdString == "n2.4" || stdString == "802.11n2.4"
	         || stdString == "n5" || stdString == "802.11n5"
	         || stdString == "n" || stdString == "802.11n")
		*target = WIFI_STANDARD_80211n;
	else if (stdString == "ac" || stdString == "802.11ac")
		*target = WIFI_STANDARD_80211ac;
	else if (stdString == "ax2.4" || stdString == "802.11ax2.4"
	         || stdString == "ax5" || stdString == "802.11ax5"
	         || stdString == "ax" || stdString == "802.11ax")
		*target = WIFI_STANDARD_80211ax;
	else {
		cerr << "Error:  Wifi standard \"" << stdString
		     << "\" unknown.\n";
		return false;
	}
	return true;
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
	if (cfg.default_channel) {
		*helper = YansWifiChannelHelper::Default();
		return true;
	}

	// Set delay model
	if (cfg.delay_model.type_name == "") {
		helper->SetPropagationDelay("ns3::ConstantSpeedPropagationDelayModel");
	} else {
		// Use simple type name without custom attributes for new API
		helper->SetPropagationDelay(cfg.delay_model.type_name);
	}

	// Apply propagation loss models
	for (int i = 0; i < int(cfg.loss_model.size()); ++i) {
		if (cfg.loss_model[i].type_name == "@matrix") {
			// We handle the pseudo-ns3 loss model called
			// "@matrix" separately to create loss models.
			cerr << "Error:  @matrix loss not implemented.\n";
			return false;
		} else {
			// Use simple type name without custom attributes for new API
			helper->AddPropagationLoss(cfg.loss_model[i].type_name);
		}
	}
	return true;
}

bool configureWifiPhy(ns3::YansWifiPhyHelper* phy,
		      const wifiConfig& cfg)
{
	// In modern NS-3, dual-band standards (802.11n, 802.11ax) require
	// explicit band specification via ChannelSettings on the PHY.
	// Single-band standards (a=5GHz, b/g=2.4GHz, ac=5GHz) are unambiguous.
	const std::string& std = cfg.wifi_standard;
	if (std == "n2.4" || std == "802.11n2.4") {
		phy->Set("ChannelSettings", ns3::StringValue("{0, 0, BAND_2_4GHZ, 0}"));
	} else if (std == "n5" || std == "802.11n5"
	           || std == "n" || std == "802.11n") {
		phy->Set("ChannelSettings", ns3::StringValue("{0, 0, BAND_5GHZ, 0}"));
	} else if (std == "ax2.4" || std == "802.11ax2.4") {
		phy->Set("ChannelSettings", ns3::StringValue("{0, 0, BAND_2_4GHZ, 0}"));
	} else if (std == "ax5" || std == "802.11ax5"
	           || std == "ax" || std == "802.11ax") {
		phy->Set("ChannelSettings", ns3::StringValue("{0, 0, BAND_5GHZ, 0}"));
	}
	// Note: 80211a=5GHz only, 80211b/g=2.4GHz only, 80211ac=5GHz only
	// — those are unambiguous and NS-3 picks the correct band automatically.

	for (const auto& a : cfg.phy_attribs) {
		if (!SetFactoryAttributeByAssignmentSpec(phy, a)) {
			return false;
		}
	}

	return true;
}
