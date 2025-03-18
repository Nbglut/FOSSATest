/**
 * Sketch License Agreement
 * 
 * This License pertains to the sketch "Seductive Man of the Ocean and the Night" created by Ryan Russell
 * 
 * This Sketch License Agreement grants permission to use the sketch described below (the "Sketch") for the purposes outlined in section 2
 * 
 * 1) Description of the Sketch:
 *      Title: Seductive Man of the Ocean and the Night
 *      Visual Description: Man with face painted half blue and half black with various markings.
 * 
 * 2) Purpose of Use
 *      Recipient of license may use the Sketch in whatever way they may see fit so long as credit for the original work is given to its creator, Ryan Russell
 */


// BEGIN COPYRIGHTED WORK - Used with permission granted by license above

// THE FOLLOWING CODE IS PROPERTY OF CHASE PACKER Copyright © 2023 DO NOT USE WITHOUT EXPLICIT PERMISSION FROM OWNER

class RuVerb {
    constructor(kan, hira, roma, mean) {
      this.type = 2;
      this.kanji = kan;
      this.hiragana = hira;
      this.romanji = roma;
      this.meaning = mean;
    }
  
    cutRu(result) {
      return result.substring(0, result.length - 2);
    }
  
    //Normal Form-------------------------------------------------------------------
  
    norPresPosForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "masu";
      return result;
    }
  
    norPresPosCasNor() {
      return this.romanji;
    }
  
    norPresNegForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "masen";
      return result;
    }
  
    norPresNegCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "nai";
      return result;
    }
  
    norPastPosForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "mashita";
      return result;
    }
  
    norPastPosCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "ta";
      return result;
    }
  
    norPastNegForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "masendeshita";
      return result;
    }
  
    norPastNegCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "nakatta";
      return result;
    }
  
    norTe() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "te";
      return result;
    }
  
    norTara() {
      return this.norPastPosCasNor() + "ra";
    }
  
    norTari() {
      return this.norPastPosCasNor() + "ri";
    }
  
    norBa() {
      let result = this.romanji;
      result = result.substring(0, result.length - 1);
      result += "eba";
      return result;
    }
  
    //Potential Form-------------------------------------------------------------
  
    potPresPosForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "raremasu";
      return result;
    }
  
    potPresPosCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "rareru";
      return result;
    }
  
    potPresNegForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "raremasen";
      return result;
    }
  
    potPresNegCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "rarenai";
      return result;
    }
  
    potPastPosForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "raremashita";
      return result;
    }
  
    potPastPosCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "rareta";
      return result;
    }
  
    potPastNegForNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "raremasendeshita";
      return result;
    }
  
    potPastNegCasNor() {
      let result = this.romanji;
      result = this.cutRu(result);
      result += "rarenakatta";
      return result;
    }
  
    potTe()
    {
      let result = this.potPresPosCasNor();
      result = this.cutRu(result);
      result += "te";
      return result;
    }
  
    potTara() {
      return this.potPastPosCasNor() + "ra";
    }
  
    potTari() {
      return this.potPastPosCasNor() + "ri";
    }
  
    potBa() {
      let result = this.potPresPosCasNor();
      result = result.substring(0, result.length - 1);
      result += "eba";
      return result;
    }
  
    //Passive Form--------------------------------------------------------------
  
    pasPresPosForNor() {
      return this.potPresPosForNor();
    }
  
    pasPresPosCasNor() {
      return this.potPresPosCasNor();
    }
  
    pasPresNegForNor() {
      return this.potPresNegForNor();
    }
  
    pasPresNegCasNor() {
      return this.potPresNegCasNor();
    }
  
    pasPastPosForNor() {
      return this.potPastPosForNor();
    }
  
    pasPastPosCasNor() {
      return this.potPastPosCasNor();
    }
  
    pasPastNegForNor() {
      return this.potPastNegForNor();
    }
}