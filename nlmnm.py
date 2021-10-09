logic_gates_help = str('''
*****************************************************************
*   NOT gate
*  X →→→►●→→→ X'
*
*  The NOT gate is also called the inverter its function is
*                        a === a'
*  It inverts the input. 0 === 1.It only takes one input
*  its number of inputs is 2¹.
******************************************************************
*   AND gate
*  a ___
*  b ___█Ɒ→→→  a.b
*
*  The AND gate is also called the multiplier its function is
*                        (a, b) === a.b
*  It multiplies the input. (1,1) === 1, (0,0)=== 0, (1,0)===0
*  The number of outputs is two to the power number of inputs
******************************************************************
*   OR gate
*       ___
*  a ---)   )
*        )OR )→→ a+b
*  b ---)___)
*
*  The OR gate is also called the sigma its function is
*                        (a, b) === a+b
*  It adds the input. (1,1) === 1, (0,0)=== 0, (1,0)===1
*  The number of outputs is two to the power number of outputs
******************************************************************
*   NAND gate
*  a ___
*  b ___█Ɒ●→→  (a.b)'
*
*  The AND gate states multiply then invert its function is
*                        (a, b) === (a.b)'
*  It multiplies the input and the inverts the result.
*  (1,1) === 0, (0,0)=== 1, (1,0)===1
*  The number of outputs is two to the power number of inputs
******************************************************************
*   NOR gate
*        ___
*  a ---)   )
*        )OR )●→→ (a+b)'
*  b ---)___)
*
*  The NOR gate states add then invert its function is
*                        (a, b) === (a+b)'
*  It adds the input and the inverts the result.
*  (1,1) === 0, (0,0)=== 1, (1,0)===0
*  The number of outputs is two to the power number of inputs
******************************************************************
*   Exclusive OR XOR
*         ___
*  a ---))   )
*        ))OR )→→ a.b' + a'.b
*  b ---))___)
*
******************************************************************
*   Exclusive NOR XNOR
*         ___
*  a ---))   )
*        ))OR )●→→ a'.b' + a'.b
*  b ---))___)
*
******************************************************************
''')















