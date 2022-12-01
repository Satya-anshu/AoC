internal class Program
{
    private static List<long> GetTotal()
    {
        List<long> total = new List<long>();
        long current_sum = 0;
        using (StreamReader sr = new StreamReader("input.txt"))
        {
            string line;

            while ((line = sr.ReadLine()) != null)
            {
                if (line != "")
                {
                    long num = long.Parse(line);
                    current_sum += num;
                }
                else
                {
                    total.Add(current_sum);
                    current_sum = 0;
                }
            }
            total.Sort();
            total.Reverse();
            return total;
        }
    }

    private static void Main(string[] args)
    {
        List<long> total = GetTotal();

        Console.WriteLine("Part 1: " + total.First());
        Console.WriteLine("Part 2: " + total.Take(3).Sum());
    }
}