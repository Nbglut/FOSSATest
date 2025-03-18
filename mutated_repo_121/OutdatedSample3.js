/**
  Copyright (c) 1996-2000 Intel Corporation
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of the Intel Corporation nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE INTEL OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

EXPORT LAWS: THIS LICENSE ADDS NO RESTRICTIONS TO THE EXPORT LAWS OF YOUR JURISDICTION. It is licensee's responsibility to comply with any export regulations applicable in licensee's jurisdiction. Under CURRENT (May 2000) U.S. export regulations this software is eligible for export from the U.S. and can be downloaded by or otherwise exported or reexported worldwide EXCEPT to U.S. embargoed destinations which include Cuba, Iraq, Libya, North Korea, Iran, Syria, Sudan, Afghanistan and any other country to which the U.S. has embargoed goods and services.
 **/


// BEGIN COPYRIGHTED WORK - Used with permission granted by license above

/**
 * This file handles the code related to handling user input in Conjugation Practice. It listens for enter inputs by the user
 * and edits the UI to reflect the state of the practice and works with "conjPracQGen.js" to generate the conjugation questions
 * and check the user's answers.
 * 
 * Author: Chase Packer
 */


//Handle User Input--------------------------------------------------------------------

var correct = 0;
var questions = 0;
let percent = 100;


var active = true;


/**
 * This function is called when the user presses enter after filling 
 * in their response to the prompted conjugation question.
 * 
 * Checks the provided response and changes the relevant HTML elements 
 * to inform the user of the correctness of their answer.
 */
function checkAnswer()
{

    console.log("Checking user response");

    var input = document.getElementById("stringInput").value;//get user response

    console.log("User Response is: " + input);

    input = hiraganaParser(input);//Answer could be written in hiragana, so convert it to romanji

    console.log("Romanji Response is: " + input);

    questions += 1;//increment the question counter for accuracy percentage


    //Hide HTML elements related to response input
    document.getElementById("stringInput").value = "";
    document.getElementById("stringInput").classList.add("hidden");
    document.getElementById("enterButton").classList.add("hidden");


    //check accuracy of answer       
    var res = input == answer;


    if(res == true)//correct
    {
        console.log("User Response is correct:  " + input + " = " + answer);
        document.getElementById("result").innerText = "Correct";
        document.getElementById("answer").innerText = romanjiParser(answer) + " " + answer;
        correct += 1;
    }
    else
    {
        console.log("User Response is incorrect:  " + input + " != " + answer);
        document.getElementById("result").innerText = "Incorrect";
        document.getElementById("answer").innerText = "The correct answer is: " + romanjiParser(answer) + " " + answer;
    }

    //recalculate percent and update it on the page     
    percent = correct / questions * 100;
    document.getElementById("percentage").innerText = percent + "%";
    active = false;//reset active flag so enter works properly
}


document.addEventListener("keydown", handleArrowKey);

/**
 * Listens for enter key press from user.
 * 
 * If user is currently answering a question (active is true), pressing enter will check user's response and
 * change the display to show the correctness of the user's response.
 * 
 * If user is looking at the result (active is false), pressing enter will change the screen back to the input
 * "screen" and generate the next question.
 * 
 * @param {*} event listens for enter key
 */
function handleArrowKey(event) {
    if (event.key === "Enter") {

        
                
        if(active == true)//Currently in input screen
        {
            console.log("Enter Pressed, Checking Answer");
            checkAnswer();
        }
        else//Currently on result screen
        {
            console.log("Enter Pressed, Going to next question");
            active= true;
            document.getElementById("stringInput").classList.remove("hidden");
            document.getElementById("enterButton").classList.remove("hidden");
                    
            generateQ();
            document.getElementById("result").innerText = "";
            document.getElementById("answer").innerText = "";
        }
                

    } 
            

}


generateQ();//Generate question for when the page initializes