namespace Microsoft.Samples 
{
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation HelloQ() : Result
    {
        Message($"Hello from quantum world!"); 
        return Zero;
    }
}