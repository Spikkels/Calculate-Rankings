import unittest

import sys
import os
sys.path.append("..")
from src.application.CalculateRankings import CalculateRankings

cwd = os.getcwd()

class TestCalculateRankings(unittest.TestCase):
    def setUp(self):
        self.manualInput = CalculateRankings()

    ###################
    ###################  isResultsAvailable tests
    ################### 
    def test_no_rankings_results_should_be_available(self):
        result = self.manualInput.isResultsAvailable()

    def test_rankings_results_should_be_available(self):
        input: list(str) = ["England 2, France 2"] 
        self.manualInput.inputGameResultsFromInput(input)
        result = self.manualInput.isResultsAvailable()

        self.assertEqual(result, True)

    ###################
    ###################  Manual input single line tests
    ################### 
    def test_manual_input_single_line_valid1(self):
        input: list(str) = ["England 2, France 2"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, True)

    def test_manual_input_single_line_valid2(self):
        input: list(str) = ["England 2, France MC 3"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, True)

    def test_manual_input_single_line_valid3(self):
        input: list(str) = ["England MC 2, France MC 3"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, True)

    def test_manual_input_single_line_valid_invalid1(self):
        input: list(str) = ["England"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, False)

    def test_manual_input_single_line_valid_invalid2(self):
        input: list(str) = ["England 2"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, False)

    def test_manual_input_single_line_valid_invalid3(self):
        input: list(str) = ["England 2 Spain 5"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, False)

    def test_manual_input_single_line_valid_invalid_same_name2(self):
        input: list(str) = ["England 2, England 4"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, False)

    def test_manual_input_single_line_valid_invalid_no_score1(self):
        input: list(str) = ["England gg, England gg"] 
        result = self.manualInput.inputGameResultsFromInput(input)

        self.assertEqual(result, False)

    ###################
    ###################  Manual input multi line tests
    ################### 
    def test_manual_input_multi_line_valid1(self):
        input1: list(str) = ["England 2, France 2"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, True)

    def test_manual_input_multi_line_valid2(self):
        input1: list(str) = ["England 2, France MC 3"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, True)

    def test_manual_input_multi_line_valid3(self):
        input1: list(str) = ["England MC 2, France MC 3"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, True)

    def test_manual_input_multi_line_valid_invalid1(self):
        input1: list(str) = ["England"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, False)

    def test_manual_input_multi_line_valid_invalid2(self):
        input1: list(str) = ["England 2"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, False)

    def test_manual_input_multi_line_valid_invalid3(self):
        input1: list(str) = ["England 2 Spain 5"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, False)

    def test_manual_input_multi_line_valid_invalid_same_name2(self):
        input1: list(str) = ["England 2, England 4"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, False)

    def test_manual_input_multi_line_valid_invalid_no_score1(self):
        input1: list(str) = ["England gg, England gg"] 
        input2: list(str) = ["Spain 2, France 2"]
        result = self.manualInput.inputGameResultsFromInput(input1 + input2)

        self.assertEqual(result, False)

    ###################
    ###################  Import input single line tests
    ################### 
    def test_import_input_single_line_valid1(self):
        result = self.manualInput.inputGameResultsFromFile("valid_game_results.txt")
        self.assertEqual(result, True)

    def test_import_input_single_line_valid2(self):
        result = self.manualInput.inputGameResultsFromFile("invalid_game_results.txt")
        self.assertEqual(result, False)


    ###################
    ###################  Import input single line tests
    ################### 
    def test_ranking_Basic_Basic1(self):
        input1: list(str) = ["AAAA 4, BBBB 0"]

        self.manualInput.inputGameResultsFromInput(input1)
        result = self.manualInput.calculateRankings()
        self.assertEqual(result, '1. AAAA: 3 pts\n2. BBBB: 0 pts')

    def test_ranking_Basic_Basic2(self):
        input1: list(str) = ["AAAA 2, BBBB 2"]

        self.manualInput.inputGameResultsFromInput(input1)
        result = self.manualInput.calculateRankings()
        self.assertEqual(result, '1. AAAA: 1 pts\n1. BBBB: 1 pts')

    def test_ranking_results_sorting1(self):
        input1: list(str) = ["AAAA 2, BBBB 3"] 
        input2: list(str) = ["CCCC 2, DDDD 2"]
        input3: list(str) = ["AAAA 2, DDDD 3"] 
        input4: list(str) = ["EEEE 2, AAAA 2"]
        input5: list(str) = ["EEEE 2, DDDD 3"] 

        self.manualInput.inputGameResultsFromInput(input1 + input2 + input3 + input4 + input5)
        result = self.manualInput.calculateRankings()
        self.assertEqual(result, '1. DDDD: 7 pts\n2. BBBB: 3 pts\n3. AAAA: 1 pts\n3. CCCC: 1 pts\n3. EEEE: 1 pts')

    def test_ranking_results_sorting2(self):
        input1: list(str) = ["AAAA 2, BBBB 3"]
        input2: list(str) = ["CCCC 2, DDDD 2"]
        input3: list(str) = ["AAAA 2, DDDD 3"]
        input4: list(str) = ["EEEE 2, AAAA 2"]
        input5: list(str) = ["EEEE 2, DDDD 3"]

        self.manualInput.inputGameResultsFromInput(input5 + input4 + input3 + input2 + input1)
        result = self.manualInput.calculateRankings()
        self.assertEqual(result, '1. DDDD: 7 pts\n2. BBBB: 3 pts\n3. AAAA: 1 pts\n3. CCCC: 1 pts\n3. EEEE: 1 pts')

