/**
 * Copyright © 2023 Chase Packer
 * License granted for unlimited use of copyrighted work included below for a limited duration, starting on Nov 5, 2023 and concluding on Nov 6 2023.
 * Use of the Work outside of this time frame is prohibited.
 */


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