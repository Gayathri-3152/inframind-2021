// SPDX-License-Identifier: GPL-3.0

pragma solidity 0.4.25;
pragma experimental ABIEncoderV2;

contract Array {
    string[] public user;
    uint[] public systolicBloodPressure;
    uint[] public diastolicBloodPressure;
    uint[] public bodyTemperature;
    uint[] public oxygenSaturation;
    uint[] public heartRate;
    uint[] public respirationate;
    uint[] public bloodGlucose;
    
    function getdata(string h, uint i, uint j, uint k, uint l, uint m, uint n, uint o) public {
         user.push(h);
         systolicBloodPressure.push(i);
         diastolicBloodPressure.push(j);
         bodyTemperature.push(k);
         oxygenSaturation.push(l);
         heartRate.push(m);
         respirationate.push(n);
         bloodGlucose.push(o);
    }
    
    function retrievedata() public view returns (string[] , uint[],uint[], uint[], uint[], uint[], uint[], uint[] ){
        return (user, systolicBloodPressure, diastolicBloodPressure, bodyTemperature,oxygenSaturation, heartRate, respirationate,bloodGlucose);
    }
   

}
   