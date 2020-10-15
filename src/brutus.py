""" Brutus: A simple password-protected password brute-force support tool

Brutus provides a simple interface for you to run a binary or script and test a password, simplifying the task of breaking passwords with brute force.

"""
import pexpect
import time

class Binary:
    """ Represents a binary file for cracking and allows it to be run with given input and a test for correct/incorrect password """
    def __init__(self,path,options=[]):
        """ Initialises the binary

        Args:
            path: the absolute or relative path of the binary
            options: an option list of options that are to be given to the binary on execution
        """
        self.path=path
        self.options=options
        self.proc=None
        self.queue=[]

    def run(self):
        """ Begins executing the binary. Returns as soon as it has been launched. """
        argv=[self.path]+self.options
        self.proc=child = pexpect.spawn(" ".join(argv))
        
    def read(self):
        """ Reads data from the standard output of the binary.
        Returns:
            None: if there is no data
            A String: containing the next line of output if available."""

        self.proc.expect(prompt)
        self.proc.send(data+"\n")
        try:
            self.proc.expect(fail, timeout=2)
            return False
        except pexpect.exceptions.EOF:
            return True

        
    def attempt(self,prompt,data, fail):
        """ Make a guess at a password, when the expected prompt is found
        Args:
            prompt: a string to idenitfy in the output that signifies WHEN to make the attempt
            data: a string to send as the password guess
            fail: the text expected on a failed attempt
        Returns:
            True: If the failure text *IS NOT* found in the output after the attempt
            False: If the failure text *IS* found in the output after the attempt
        """
        self.proc.expect(prompt)
        self.proc.send(data+"\n")
        try:
            self.proc.expect(fail, timeout=2)
            return False
        except pexpect.exceptions.EOF:
            return True


    def timedAttempt(self,prompt,data,fail):
        """ Make a guess at a password, when the expected prompt is found
        Args:
            prompt: a string to idenitfy in the output that signifies WHEN to make the attempt
            data: a string to send as the password guess
            fail: the text expected on a failed attempt
        Returns:
            a tuple in which the first item is:

              - True: If the failure text *IS NOT* found in the output after the attempt

              - False: If the failure text *IS* found in the output after the attempt

            and the second item is the number of fractional seconds the guess took to make
        """
        t1=time.perf_counter()
        result=self.attempt(prompt,data,fail)
        t2=time.perf_counter()
        return (result,t2-t1)
